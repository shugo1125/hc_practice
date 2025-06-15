const calendar_display = (year, month) => {
  console.log(`      ${month}月 ${year}`);
  const weeks = ["日", "月", "火", "水", "木", "金", "土"];
  console.log(weeks.join(" "));
  const startday = new Date(year, month - 1, 1).getDay();

  const monthdays = new Date(year, month, 0).getDate();

  const result = [];
  const blank = String(" ").padStart(2, " ");

  for (let index = 0; index < startday; index++) {
    process.stdout.write("   ");
  }

  let space = startday;
  for (let day = 1; day <= monthdays; day++) {
    process.stdout.write(String(day).padStart(2, " ") + " ");
    space = (space + 1) % 7;
    if (space === 0) console.log();
  }
  if (space !== 0) console.log();
  console.log();
};
const [, , optionKey, optionValue] = process.argv;
const year = new Date().getFullYear();
let month;

if (optionKey === "-m") {
  const parsedMonth = parseInt(optionValue, 10);
  if (isNaN(parsedMonth) || parsedMonth < 1 || parsedMonth > 12) {
    console.log("不正な入力値です。1〜12の数字を指定してください。");
    process.exit(1);
  }
  month = parsedMonth;
} else {
  month = new Date().getMonth() + 1;
}

calendar_display(year, month);
