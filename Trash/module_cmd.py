#!/usr/bin/env python3

import cmd

class HelloWorld(cmd.Cmd):
    """Simple Command Processor Beispiel"""

    FRIENDS = [ 'Alice', 'Adam', 'Barbara', 'Bob' ]
    prompt = '(hbnb) '
    doc_header = 'You fuckers lucky I am here'
    undoc_header = 'Real lucky mfers'
    misc_header = 'Wo ist hier'
    ruler = '-x-><-x-'
    intro = 'Wilkommen'

    def do_greet(self, person):
        if person and person in self.FRIENDS:
            print("Hi " + person)
        elif person:
            print("Servus " + person)
        else:
            print("Hallo Dort")

    def complete_greet(self, text, line, begidx, endidx):
        if not text:
            completions = self.FRIENDS[:]
        else:
            completions = [f
                            for f in self.FRIENDS
                            if f.startswith(text)
                            ]
            return completions

    def help_greet(self):
        print('\n'.join(['greet [person]',
                            'Greet the named person',
                            ]))
    def do_EOF(self, line):
        return True

    def postloop(self):
        print("Tschuss")

if __name__ == '__main__':
    HelloWorld().cmdloop()
