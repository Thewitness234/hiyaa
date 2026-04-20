letter = ''' Dear <|Name|>,
            You are selected!
            <|Date|>'''
print(letter.replace("<|Name|>", "raman").replace("<|Date|>", "12"))