#!/usr/bin/env  python3

import sys
import json
import os

# make sure to do an __init__ method

  

class Tasty:
    """
    Tasty class.
    :param tasks: the user tasks
    :param important_tasks: the important user tasks
    :param complete: the completed tasks
    :param unfinished: the unfinished tasks
    :param trash: the user trash
    :param version: the Tasty version
    :param save_file: the Tasty save file
    """
    # make sure to do an __init__ method
    
    def __init__(self):
        self.tasks = {}
    
   
    def add_task(self, task_name):
        if task_name not in self.tasks:
            self.tasks[task_name] = "not yet"  
        else:
            print("Task already added.")    

    def prompt_user(self, prompt):
        line = input(prompt)
        #print(line) 
        while not line:
            line = input(prompt) 
        words = line.split()
        #print(words)
        command = words[0] 
        #print(command) 
        rest = words[1:] 
        rest = " ".join(rest)
        #print(rest)
        return command, rest      

    def display_tasks(self):
        if self.tasks:
            for task_name, status in self.tasks.items():
                print("- ", task_name, status)        
        else:
            print("You have no task.")

    def remove_task(self, task_name):
        if task_name in self.tasks:
            del self.tasks[task_name]
        else:
            print("Task not found.")   

    #def tasks(self, task_name = None):
       #task_name = input("Please enter the task you want to perform:")
       #self.task_name.append(task_name)
       #print(f"Task '{task_name}' preparing.")

    
    #def new_task(self):
       # if not self.tasks:
       #      print("No tasks found.")
        #else:
         #   input("please enter the new task that you want to perform:") 
        

    def help(self):
        """
        Display a help message.
        """
        print("Tasty Help ")
        print("============================================================================")
        print("help                     ->        display this message")
        print("tasks                    ->        display all your tasks")
        print("trash                    ->        display the content of the trash")
        print("new <task>               ->        add a new task")
        print("remove <task>            ->        add a task to the trash")
        print("complete <task>          ->        complete a task")
        print("unfinish <task>          ->        unfinish a task")
        print("recover <task>           ->        recover a removed task")
        print("destroy <task>           ->        remove a task from the trash")
        print("advancement              ->        see the tasks advancement")
        print("exit                     ->        exit Tasty")
        print("save                     ->        save your current tasks")
        print("load                     ->        load a save file")
        print("clear                    ->        clear the screen")
        


    def exitScreen(self):
        print("Bye! Exiting Tasty program.")
        exit() 

    def clearScreen(self):
        os.system('cls' if os.name == 'nt' else 'clear')  

    def license(self):
        """
        Display the MIT License terms for Tasty.
        """
        print("""
Copyright (c) 2024 Tasty

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
        """)


if __name__ == "__main__":
    tasty = Tasty()
    tasty.help()

    while True:
        command, task_name = tasty.prompt_user("Tasty> ")
        if command == "exit":
            tasty.exitScreen() # exit the program, how woud you do this?
        elif command == "help":
            tasty.help()
        elif command == "new":
            tasty.add_task(task_name)
        elif command == "remove":
            tasty.remove_task(task_name)
        elif command == "tasks":
            tasty.display_tasks()    
        elif command == "load":
            tasty.load()
        elif command == "license":
            tasty.license()
        elif command == "clear screen":
            tasty.clearScreen()
        else:
            print("Unknown command:", command, task_name)