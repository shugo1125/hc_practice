// Dangerfile.js

if (danger.github.pr.additions + danger.github.pr.deletions > 200) {
  warn("このPRは200行以上の変更があります。細かく分割しましょう。");
}

if (danger.github.pr.changed_files > 10) {
  warn("このPRは10ファイル以上を変更しています。分割した方が良いかもしれません。");
}