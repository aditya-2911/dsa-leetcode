class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        idx = 0
        n = len(expression)
        
        def parse_expr() -> set:
            nonlocal idx
            res = set(parse_term())
            
            while idx < n and expression[idx] == ',':
                idx += 1
                res.update(parse_term())
                
            return res
            
        def parse_term() -> set:
            nonlocal idx
            res = {""}
            while idx < n and (expression[idx].isalpha() or expression[idx] == '{'):
                factor_res = parse_factor()
                new_res = set()
                for a in res:
                    for b in factor_res:
                        new_res.add(a + b)
                res = new_res
                
            return res
            
        def parse_factor() -> set:
            nonlocal idx
            if expression[idx].isalpha():
                start = idx
                while idx < n and expression[idx].isalpha():
                    idx += 1
                return {expression[start:idx]}
                
            elif expression[idx] == '{':
                idx += 1
                res = parse_expr()
                idx += 1               
                return res
                
        return sorted(list(parse_expr()))