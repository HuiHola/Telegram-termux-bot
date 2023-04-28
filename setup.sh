apt install python3 -y
pip install python-telegram-bot
apt install termux-api
printf "\033[94mDo you want to download termux-api.apk \033[91m(necessary) \033[94m(y or n): ";read opt

if [ $opt == "y" ]
then
	xdg-open https://f-droid.org/repo/com.termux.api_51.apk
fi

echo -e "\033[92minstalling done.\033[0m"
