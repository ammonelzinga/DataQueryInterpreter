from .fsa_classes.fsa import FSA
from .fsa_classes.colon_dash_fsa import ColonDashFSA
from .fsa_classes.colon_fsa import ColonFSA
from .fsa_classes.comma_fsa import CommaFSA
from .fsa_classes.add import AddFSA
from .fsa_classes.comment_fsa import CommentFSA
from .fsa_classes.facts_fsa import FactsFSA
from .fsa_classes.id_fsa import IdFSA
from .fsa_classes.left_paren import LeftParenFSA
from .fsa_classes.multiply import MultiplyFSA
from .fsa_classes.period_fsa import PeriodFSA
from .fsa_classes.q_mark_fsa import QMarkFSA
from .fsa_classes.queries_fsa import QueriesFSA
from .fsa_classes.right_paren import RightParenFSA
from .fsa_classes.rules_fsa import RulesFSA
from .fsa_classes.schemes_fsy import SchemesFSA
from .fsa_classes.string_fsa import StringFSA
from typing import Callable

from .token import Token

class LexerFSM:
    def __init__(self):
        self.tokens: list[Token] = []
        self.fsa_list = []
        self.status_dict: dict = dict()
        self.lineCounter = 1
        self.tokenCounter = 1
        self.colon_dash_fsa: ColonDashFSA = ColonDashFSA()
        self.fsa_list.append(self.colon_dash_fsa)
        self.colon_fsa: ColonFSA = ColonFSA()
        self.fsa_list.append(self.colon_fsa)
        self.comma = CommaFSA()
        self.fsa_list.append(self.comma)
        self.add = AddFSA()
        self.fsa_list.append(self.add)
        self.comment = CommentFSA()
        self.fsa_list.append(self.comment)
        self.facts = FactsFSA()
        self.fsa_list.append(self.facts)
        self.id_fsa = IdFSA()
        self.fsa_list.append(self.id_fsa)
        self.left_paren = LeftParenFSA()
        self.fsa_list.append(self.left_paren)
        self.multiply = MultiplyFSA()
        self.fsa_list.append(self.multiply)
        self.period = PeriodFSA()
        self.fsa_list.append(self.period)
        self.q_mark = QMarkFSA()
        self.fsa_list.append(self.q_mark)
        self.queries = QueriesFSA()
        self.fsa_list.append(self.queries)
        self.right_paren = RightParenFSA()
        self.fsa_list.append(self.right_paren)
        self.rules = RulesFSA()
        self.fsa_list.append(self.rules)
        self.schemes = SchemesFSA()
        self.fsa_list.append(self.schemes)
        self.string = StringFSA()
        self.fsa_list.append(self.string)
        # other FSA classes and any other member variables you need
    
    def run(self, input: str) -> str:
        print('hello000')
        potential_string = False
        answer = ''
        characters_gobbled = 0
        i = 0
        while characters_gobbled + 1 < len(input) and i+1 < len(input):
            while input[characters_gobbled].isspace():
                if input[characters_gobbled] == '\n': 
                    self.lineCounter +=1
                characters_gobbled +=1
                if characters_gobbled == len(input):
                    #print(f'number of tokens: {len(self.tokens)}')
                    for the_token in self.tokens: 
                        answer = answer + the_token.to_string() + '\n'
                        #print('hello????')
                        self.tokenCounter +=1
                    answer = answer + (f'(EOF,"",{self.lineCounter})') + '\n'
                    answer = answer + (f'Total Tokens = {self.tokenCounter}')
                    self.tokens.append(Token('EOF', "", self.tokenCounter))
                    return self.tokens
                    #return answer
            i = characters_gobbled + 1
            input_string = input[characters_gobbled:i]
            if input_string == "'":
                potential_string = True
            if self.lex(input_string) != False:
                while self.lex(input[characters_gobbled:i+1]) != False:
                    #print(input[characters_gobbled:i+2])
                    i += 1 
                input_string = input[characters_gobbled:i]
                self.lex(input_string)
                #print(input_string)
                characters_gobbled = i
                #print(f'gonna append {input_string}')
                self.tokens.append(self.__manager_fsm__(input_string, self.lineCounter))
                
            elif potential_string == True:
                potential_string = False
                #print('potentialstring')
                found_string = 'zingaboy'
                char = characters_gobbled
                istring = i
                irealstring = i 
                while (istring + 1) < len(input) and input[(istring-1)] != '\n': 
                    if self.lex(input[char:istring]) == True: 
                        found_string = input[char:istring]
                        irealstring = istring
                    istring += 1
                if found_string != 'zingaboy': 
                    input_string = found_string
                    #i = irealstring
                    self.lex(input_string)
                    #print(input_string)
                    characters_gobbled = irealstring
                    #print(f'gonna append {input_string}')
                    self.tokens.append(self.__manager_fsm__(input_string, self.lineCounter))
                    potential_string = False
                else:
                    #print(input_string)
                    for toke in self.tokens: 
                        answer = answer + toke.to_string() + '\n'
                        self.tokenCounter += 1
                    answer = answer + (f'(UNDEFINED,"{input_string}",{self.lineCounter})') + '\n' + '\n'
                    answer = answer + (f'Total Tokens = Error on line {self.lineCounter}')
                    return answer  #FIX THIS LINE, is it supposed to be a raiseError?
            else: 
                #print(input_string)
                for toke in self.tokens: 
                    answer = answer + toke.to_string() + '\n'
                    self.tokenCounter += 1
                answer = answer + (f'(UNDEFINED,"{input_string}",{self.lineCounter})') + '\n' + '\n'
                answer = answer + (f'Total Tokens = Error on line {self.lineCounter}')
                return answer  #FIX THIS LINE, is it supposed to be a raiseError?
        #print(f'number of tokens: {len(self.tokens)}')
        for the_token in self.tokens: 
            answer = answer + the_token.to_string() + '\n'
            #print('hello?')
            #print(answer)
            self.tokenCounter +=1
        answer = answer + (f'(EOF,"",{self.lineCounter})') + '\n'
        answer = answer + (f'Total Tokens = {self.tokenCounter}')
        self.tokens.append(Token('EOF', "", self.tokenCounter))
        #print(answer)
        return self.tokens
        #return answer
    
    def lex(self, input_string: str) -> Token:
        tokens_found = 0
        token_name = ''
        for automatan in self.fsa_list: 
            if (automatan).run(input_string)== True: 
                token_name = automatan.get_name()
                self.status_dict[token_name] = True
                 #might need to make that an f string
                tokens_found +=1
                for new_line_counter in input_string: 
                    if new_line_counter == '\n': 
                        self.lineCounter +=1
                        #print('new lineee')
            else: 
                self.status_dict[automatan.get_name()] = False

        if tokens_found > 0: 
            return True
        else: return False

    def __manager_fsm__(self, input_string, line_number) -> Token:
        ...#make this call token class?
        if self.status_dict['COMMA'] == True:
            #print('comma')
            return Token('COMMA', input_string, line_number)
        elif self.status_dict['PERIOD'] == True: 
            #print('period')
            return Token('PERIOD', input_string, line_number)
        elif self.status_dict['Q_MARK'] == True: 
            #print('q_mark')
            return Token('Q_MARK', input_string, line_number)
        elif self.status_dict['LEFT_PAREN'] == True: 
            return Token('LEFT_PAREN', input_string, line_number)
        elif self.status_dict['RIGHT_PAREN'] == True: 
            return Token('RIGHT_PAREN', input_string, line_number)
        elif self.status_dict['COLON'] == True:
            if self.status_dict['COLON_DASH'] == True: 
                return Token('COLON_DASH', input_string, line_number)
            else: return Token('COLON', input_string, line_number)
        elif self.status_dict['COLON_DASH'] == True: 
            return Token('COLON_DASH', input_string, line_number)
        elif self.status_dict['MULTIPLY'] == True: 
            return Token('MULTIPLY', input_string, line_number)
        elif self.status_dict['ADD'] == True: 
            return Token('ADD', input_string, line_number)
        elif self.status_dict['SCHEMES'] == True: 
            return Token('SCHEMES', input_string, line_number)
        elif self.status_dict['FACTS'] == True: 
            return Token('FACTS', input_string, line_number)
        elif self.status_dict['RULES'] == True: 
            return Token('RULES', input_string, line_number)
        elif self.status_dict['QUERIES'] == True: 
            return Token('QUERIES', input_string, line_number)
        elif self.status_dict['ID'] == True: 
            return Token('ID', input_string, line_number)
        elif self.status_dict['STRING'] == True: 
            return Token('STRING', input_string, line_number)
        elif self.status_dict['COMMENT'] == True: 
            return Token('COMMENT', input_string, line_number)
        else: return False





    def reset(self) -> None:
        ...

#if token:token when punctuation break if token token if white space also break unless string or comment