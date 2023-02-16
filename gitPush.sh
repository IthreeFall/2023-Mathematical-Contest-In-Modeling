 now=$(date "+%Y-%m-%d")
  echo "Change Directory to D:/datum/2023-Mathematical-Contest-In-Modeling"
  cd D:/datum/2023-Mathematical-Contest-In-Modeling
  echo "Starting add-commit-pull-push..."
  git add -A && git commit -m "$now" && git pull && git push
  echo "Finish!"
  read
