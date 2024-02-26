#!/bin/bash

case ${1,,} in
	nu1lspaxe | admin)
		echo "Hello, booss"
		;;
	help)
		echo "Just enter your name, please"
		;;
	*)
		echo "Come on, I don't know who you're"
esac
