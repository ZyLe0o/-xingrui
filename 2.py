import re

def reg_search(text, regex_list):
    result_list = []

    for regex_dict in regex_list:
        result = {}
        for field_name, pattern in regex_dict.items():
            # 使用 re.findall 进行匹配，支持多组匹配
            matches = re.findall(pattern, text)
            
            if not matches:
                result[field_name] = None
            elif len(matches) == 1:
                # 如果只有一个匹配结果，直接赋值
                result[field_name] = matches[0]
            else:
                # 如果多个匹配结果，赋值列表
                result[field_name] = list(matches)
        
        result_list.append(result)
    
    return result_list
