from .fsa import FSA
from typing import Callable

class FactsFSA(FSA):
    def __init__(self):
        FSA.__init__(self)
        self.set_name('FACTS')
        self.accept_states.add(self.s5)
        
    def S0(self) -> Callable:
        next_state: function = None
        if self.input_string[self.num_chars_read] != 'F': next_state = self.s_err
        else: next_state = self.s1
        self.num_chars_read += 1
        return next_state
    
    def s1(self): 
        next_state: function = None
        if self.input_string[self.num_chars_read] != 'a': next_state = self.s_err
        else: next_state = self.s2
        self.num_chars_read +=1
        return next_state
    
    def s2(self): 
        next_state: function = None
        if self.input_string[self.num_chars_read] != 'c': next_state = self.s_err
        else: next_state = self.s3
        self.num_chars_read +=1
        return next_state
    
    def s3(self): 
        next_state: function = None
        if self.input_string[self.num_chars_read] != 't': next_state = self.s_err
        else: next_state = self.s4
        self.num_chars_read +=1
        return next_state
    
    def s4(self): 
        next_state: function = None
        if self.input_string[self.num_chars_read] != 's': next_state = self.s_err
        else: next_state = self.s5
        self.num_chars_read +=1
        return next_state
    
    def s5(self): 
        next_state: function = self.s_err
        self.num_chars_read += 1
        return next_state
    
    def s_err(self): 
        next_state = self.s_err
        self.num_chars_read +=1 
        return next_state 