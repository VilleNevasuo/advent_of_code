
import time

def parse_workflow(wf_indicator,workflows, ratings, i):

    workflow = workflows[wf_indicator]
    segmented_workflow = workflow.split(",")
    letter = segmented_workflow[i][0]
    operator = segmented_workflow[i][1]
    stripped_workflow = segmented_workflow[i][2:]
    stripped_workflow = stripped_workflow.split(":")
    measurement = int(stripped_workflow[0])
    success_candidate = stripped_workflow[1]
    fail_candidate = segmented_workflow[1+i]
    print("workflow",wf_indicator, workflow)
    print("letter",letter)
    print("operator",operator)
    print("i", i)
    print("stripped_workflow", stripped_workflow)
    print("seg workflow", segmented_workflow)
    print("measurement", measurement)
    print("success_candidate", success_candidate)
    print("fail_candidate", fail_candidate)
    print("ratings", ratings)
    print("---------------------------")
    for rating in ratings:
        if rating[0] == letter:
            if operator == "<":
                if int(rating[1]) < measurement:
                    return success_candidate
                else:
                    if ":" not in segmented_workflow[i+1]:
                        if segmented_workflow[i+1] == "R":
                            return "R"
                        elif segmented_workflow[i+1] == "A":
                            return "A"
                        else:
                            return fail_candidate
                    else:
                        return parse_workflow(wf_indicator,workflows,ratings,i+1)
            else:
                if int(rating[1]) > measurement:
                    return success_candidate
                else:
                    if ":" not in segmented_workflow[i+1]:
                        if segmented_workflow[i+1] == "R":
                            return "R"
                        elif segmented_workflow[i+1] == "A":
                            return "A"
                        else:
                            return fail_candidate
                    else:
                        return parse_workflow(wf_indicator,workflows,ratings,i+1)
                
    

def p1():
    
    total = 0
    accepted = 0
    workflows = {}
    parts = []
    with open("input.txt") as file:
        for line in file:
            line = line.strip()
            if len(line) == 0:
                continue
            elif line[0] != "{":
                line = line.strip("}")
                line = line.split("{")
                workflows[line[0]] = line[1]
            else:
                subparts = []
                line = line.strip("}{")
                line = line.split(",")
                for el in line:
                    part = el.split("=")
                    part = (part[0],part[1])
                    subparts.append(part)
                parts.append(subparts)
    

    for ratings in parts:
        next_workflow = "in"
        while True:
            i = 0
            next_workflow = parse_workflow(next_workflow,workflows, ratings, i)
            if next_workflow == "A":
                for pair in ratings:
                    total += int(pair[1])
                print("we accepted")
                accepted += 1
                break
            if next_workflow == "R":
                print("we rejected")
                break


    return total
   




print(p1())