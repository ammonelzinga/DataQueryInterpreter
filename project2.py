#Return your program output here for grading (can treat this function as your "main")
from project1_classes.lexer_fsm import LexerFSM
from project1 import project1
from descent_parser import RDP
def project2(input: str) -> str:
    #print(input)
    #new change
    lexer: LexerFSM = LexerFSM()
    parser = RDP()
    #return lexer.run(input)
    return parser.parse_input(lexer.run(input))

def read_file_contents(filepath):
    with open(filepath, "r") as f:
        return f.read() 

#Use this to run and debug code within VS
if __name__ == "__main__":
    input_contents = read_file_contents("./project2-passoff/80/input7.txt")
    print(project2(input_contents))
