if [ -f requirements.txt ]; then
  pip install --user -r requirements.txt
  brew install --cask claude-code
fi
