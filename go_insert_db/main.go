package main

import (
	"database/sql"
	"encoding/json"
	"fmt"
	"log"
	"os"

	_ "github.com/lib/pq" // DBドライバをインポート
)

// JSONを受け取るための「型紙」
type LogEntry struct {
	User struct {
		Age  int    `json:"age"`
		Name string `json:"name"`
		Role string `json:"role"`
	} `json:"user"`
}

func main() {
	// 1. 引数チェック
	if len(os.Args) != 2 {
		fmt.Println("Error: ファイルパスを1つだけ指定してください")
		os.Exit(1)
	}
	filename := os.Args[1]

	// 2. DB接続（ポート5432！）
    connStr := "user=user password=password dbname=log_db port=5432 sslmode=disable"

	db, err := sql.Open("postgres", connStr)
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

	// 3. ログファイルを開く
	file, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	// 4. トランザクション開始
	tx, err := db.Begin()
	if err != nil {
		log.Fatal(err)
	}

	// 5. JSONを1つずつ読み込んでInsert
	decoder := json.NewDecoder(file)
	for decoder.More() {
		var entry LogEntry
		if err := decoder.Decode(&entry); err != nil {
			tx.Rollback() // 失敗したら全部キャンセル
			log.Fatalf("JSON解析エラー: %v", err)
		}

		// DBに保存
		query := "INSERT INTO users (age, name, role) VALUES ($1, $2, $3)"
		_, err := tx.Exec(query, entry.User.Age, entry.User.Name, entry.User.Role)
		if err != nil {
			tx.Rollback() // 失敗したら全部キャンセル
			log.Fatalf("Insertエラー: %v", err)
		}
	}

	// 6. すべて成功したらコミット（確定）
	if err := tx.Commit(); err != nil {
		log.Fatal(err)
	}

	fmt.Println("インポート成功！")
}