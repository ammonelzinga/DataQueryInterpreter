from .fsa import FSA
from typing import Callable

class AddFSA(FSA): 
    def __init__(self):
        FSA.__init__(self)
        self.accept_states.add(self.s1)
        self.fsa_name = 'ADD'

    def S0(self): 
        next_state: function = None
        if self.input_string[self.num_chars_read] != '+': next_state = self.s_err
        else: next_state = self.s1
        self.num_chars_read +=1 
        return next_state
    
    def s1(self): 
        next_state: function = self.s_err
        self.num_chars_read +=1 
        return next_state
    
    def s_err(self): 
        next_state: function = self.s_err
        self.num_chars_read += 1
        return next_state