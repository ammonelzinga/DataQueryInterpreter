from .fsa import FSA
from typing import Callable

class SchemesFSA(FSA):
    def __init__(self):
        FSA.__init__(self)
        self.set_name('SCHEMES')
        self.accept_states.add(self.s7)
        
    def S0(self) -> Callable:
        next_state: function = None
        if self.input_string[self.num_chars_read] != 'S': next_state = self.s_err
        else: next_state = self.s1
        self.num_chars_read += 1
        return next_state
    
    def s1(self): 
        next_state: function = None
        if self.input_string[self.num_chars_read] != 'c': next_state = self.s_err
        else: next_state = self.s2
        self.num_chars_read +=1
        return next_state
    
    def s2(self): 
        next_state: function = None
        if self.input_string[self.num_chars_read] != 'h': next_state = self.s_err
        else: next_state = self.s3
        self.num_chars_read +=1
        return next_state
    
    def s3(self): 
        next_state: function = None
        if self.input_string[self.num_chars_read] != 'e': next_state = self.s_err
        else: next_state = self.s4
        self.num_chars_read +=1
        return next_state
    
    def s4(self): 
        next_state: function = None
        if self.input_string[self.num_chars_read] != 'm': next_state = self.s_err
        else: next_state = self.s5
        self.num_chars_read +=1
        return next_state
    
    def s5(self): 
        next_state: function = None
        if self.input_string[self.num_chars_read] != 'e': next_state = self.s_err
        else: next_state = self.s6
        self.num_chars_read +=1
        return next_state
    
    def s6(self): 
        next_state: function = None
        if self.input_string[self.num_chars_read] != 's': next_state = self.s_err
        else: next_state = self.s7
        self.num_chars_read +=1
        return next_state
    
    def s7(self): 
        next_state: function = self.s_err
        self.num_chars_read += 1
        return next_state
    
    def s_err(self): 
        next_state = self.s_err
        self.num_chars_read +=1 
        return next_state 