#Return your program output here for grading (can treat this function as your "main")
from project1_classes.lexer_fsm import LexerFSM
from descent_parser import RDP
from evaluate_query import EvaluateQuery
def project4(input: str) -> str:
    lexer: LexerFSM = LexerFSM()
    parser = RDP()
    evalQuery = EvaluateQuery()
    #return lexer.run(input)
    return evalQuery.run(parser.parse_input(lexer.run(input)))
    #return ""

def read_file_contents(filepath):
    with open(filepath, "r") as f:
        return f.read() 

#Use this to run and debug code within VS
if __name__ == "__main__":
    input_contents = read_file_contents("project4-passoff/100\input8.txt")
    print(project4(input_contents))
