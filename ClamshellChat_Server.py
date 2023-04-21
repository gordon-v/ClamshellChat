import threading
import bot
import socket
import sys
import python_server

#Start the Discord Bot in a thread
if __name__ == '__main__':
	
	thread_bot = threading.Thread(target=bot.run_discord_bot)
	thread_server = threading.Thread(target=python_server.run_server)
	print("Attempting to laumch server thread")
	thread_server.start()
	print("Attempting to laumch bot thread")

	thread_bot.start()
	thread_bot.join()
	
