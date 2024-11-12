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
        self.trash = {}
        self.save_file = "saved_tasks.json"
   
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
        self.trash[task_name] = self.tasks[task_name]     
        del self.tasks[task_name]; 

    def trash_task(self):
        print(self.trash)

    def destroy_trash(self, task_name):
        if task_name in self.trash:
            del self.trash[task_name]  

    def recover_task(self, task_name):
        self.tasks[task_name] = self.trash[task_name]     
        del self.trash[task_name]; 
           
    def save_task(self):
        data = {
            "tasks": self.tasks,
        }
        with open(self.save_file, "w") as f:
            json.dump(data, f)
        print("Your task is saved.")   

    def complete_task(self, task_name):
        if self.tasks[task_name] == "task not finished yet!":
            self.tasks[task_name] = "task completed successfully!"  
        else:
            print("Task completed successfully!") 

    def unfinished_task(self, task_name):
        self.tasks[task_name] == "task is unfinished!"  

    def load_task(self):
        with open('saved_tasks.json', 'r') as fp:
            self.tasks = json.load(fp)
    
        
                


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
        print("Bye! Thanks for using Tasty program.")
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
            tasty.exitScreen() 

        elif command == "help":
            tasty.help()

        elif command == "new":
            tasty.add_task(task_name)  

        elif command == "tasks":
            tasty.display_tasks()    

        elif command == "save":
            tasty.save_task()

        elif command == "remove":
            tasty.remove_task(task_name)

        elif command == "trash":
            tasty.trash_task()  

        elif command == "destroy":
            tasty.destroy_trash(task_name)

        elif command == "recover":
            tasty.recover_task(task_name)    

        elif command == "done":
            tasty.complete_task(task_name)   

        elif command == "unfinish":
            tasty.unfinished_task(task_name)            

        elif command == "license":
            tasty.license()

        elif command == "load":
            tasty.load_task()   

        elif command == "clear":
            tasty.clearScreen()
        else:
            print("Unknown command:", command, task_name)