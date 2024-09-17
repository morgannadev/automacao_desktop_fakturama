$exclude = @("venv", "bot_fakturama.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_fakturama.zip" -Force