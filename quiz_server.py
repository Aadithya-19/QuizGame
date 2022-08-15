import socket
from threading import Thread
import random

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

server.bind((ip_address, port))
server.listen.()

list_of_clients = []

print("Server had started")

questions = [
    "What is the Italian word for pie? \n a. Mozzarella \n b. Pie \n c. Pasty \n d. torta \n"

    "How many bones are there in the human body? \n a. 206 \n b. 201 \n c. 100 \n d. 208 \n"

    "How many states are there in India? \n a. 28 \n b. 29 \n c. 31 \n d.30 \n"
]

answers = ['d', 'a', 'b']

def get_random_question(conn):
    random_index = random.randint(0, len(questions)-1)
    random_question = question[random_index]
    random_answer = answers[random_index]
    conn.send(random_question.encode('utf-8'))
    return random_index, random_question, random_answer

def remove_question(index):
    questions.pop(index)
    answers.pop(index)

def clientthread(conn):
        score = 0
        conn.send("Welcome to the Quiz Game".encode('utf-8'))
        conn.send("You will receive a question. The answer should be one of a, b, c, d")
        conn.send("Good Luck!\n\n".encode('utf-8'))
        index, question, answer = get_random_question_answer(conn)

        while True:
            try:
                message = conn.recv(2048).decode('utf-8')
                if message:
                    if message.lower()==answer:
                        score+= 1
                        conn.send(f"Bravo! Your Score is {score}\n\n".encode('utf-8'))
                    else:
                        conn.send(f"Incorrect answer! YBetter luck next time!\n\n".encode('utf-8'))
                    remove_question(index)
                    index, question, answer = get_random_question_answer(conn)
                else: 
                    remove(conn)
            except:
                continue
while True:
    conn, addr = server.accept()
    list_of_clients.append(conn)
    print (addr[0] + " connected")
    new_thread = Thread(target= clientthread,args=(conn,addr))
    new_thread.start()