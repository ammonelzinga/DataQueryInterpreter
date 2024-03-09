from .fsa import FSA
from typing import Callable


#attempting to allow lexer handle if keyword ex. "Scheme" was given
class IdFSA(FSA):
    def __init__(self):
        FSA.__init__(self)
        self.set_name('ID')
        self.accept_states.add(self.s1)

        
    def S0(self) -> Callable:
        next_state: function = None
        if (self.input_string[self.num_chars_read]).isalpha(): next_state = self.s1
        else: next_state = self.s_err
        self.num_chars_read += 1
        return next_state
    
    def s1(self): 
        next_state: function = None
        if (self.input_string[self.num_chars_read]).isalpha() or (self.input_string[self.num_chars_read]).isdigit(): next_state = self.s1
        else: next_state = self.s_err
        self.num_chars_read +=1
        return next_state
    
    def s_err(self): 
        next_state = self.s_err
        self.num_chars_read +=1 
        return next_state 