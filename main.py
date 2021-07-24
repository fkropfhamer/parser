from production_rule import ProductionRule

def main():
    production_rule1 = ProductionRule.from_string('NP -> Det N')
    production_rule2 = ProductionRule.from_string('N -> "Dinokatze"')
    production_rule3 = ProductionRule.from_string('Det -> "die"')
    
    
    print(production_rule1)
    print(production_rule2)
    print(production_rule3)


    print('end')


if __name__ == '__main__':
    main()

