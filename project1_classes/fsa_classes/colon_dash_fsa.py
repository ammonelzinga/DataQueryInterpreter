from .fsa import FSA
from typing import Callable

from .fsa import FSA
from typing import Callable

class ColonDashFSA(FSA):
    def __init__(self):
        FSA.__init__(self)
        #self.fsa_name = self.set_name('COLON_DASH')
        self.fsa_name = 'COLON_DASH'
        self.accept_states.add(self.s2)
        
    def S0(self) -> Callable:
        next_state: function = None
        if self.input_string[self.num_chars_read] != ':': next_state = self.s_err
        else: next_state = self.s1
        self.num_chars_read += 1
        return next_state
    
    def s1(self):
        next_state: function = None
        if self.input_string[self.num_chars_read] != '-': next_state = self.s_err
        else: next_state = self.s2
        self.num_chars_read +=1
        return next_state
    
    def s2(self): 
        next_state: function = self.s_err
        self.num_chars_read += 1
        return next_state
    
    def s_err(self): 
        next_state = self.s_err
        self.num_chars_read +=1 
        return next_state 
    
