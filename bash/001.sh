#!/bin/bash

if [ ${1,,} = nu1lspaxe ]; then
	echo "Welcome back, boss Nu1LSpaxe"
elif [ ${1,,} = help ]; then
	echo "Enter your name, please."
else
	echo "I don't know who you are.."
fi
