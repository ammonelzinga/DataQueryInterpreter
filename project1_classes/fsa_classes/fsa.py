from typing import Callable

class FSA:
    def __init__(self):
        self.fsa_name: str = ""
        self.start_state: function = self.S0
        self.accept_states: set[function] = set()
        self.input_string: str = ""
        self.num_chars_read: int = 0

    
    def S0(self) -> Callable:
        raise NotImplementedError()
    
    def run(self, input_string: str) -> bool:
        self.input_string = input_string
        current_state: function = self.start_state #maybe this should be self.next_state?
        while self.num_chars_read < len(self.input_string): 
            current_state = current_state()
        if current_state in self.accept_states:
            self.reset() 
            return True
        else:
            self.reset()
            return False

    def reset(self) -> None:
        self.num_chars_read = 0
        self.input_string = ""

    def get_name(self) -> str: 
        return self.fsa_name 

    def set_name(self, FSA_name) -> None:
        self.fsa_name = FSA_name

    def __get_current_input(self) -> str:  # The double underscore makes the method private
        return self.input_string[self.num_chars_read]