import src.statics


def assemble(in_file):
    ADDRESSES = dict()
    with open("./input/" + in_file, "r") as file:
        lines = file.read().split('\n')
        location = 0
        for l in lines:
            sections = l.split()
            if sections[0][-1] == ',':
                lable = sections[0]
                lable = lable[:-1]
                if location < 16:
                    ADDRESSES[lable] = "00" + hex(location).removeprefix("0x")
                    continue
                if location < 256:
                    ADDRESSES[lable] = "0" + hex(location).removeprefix("0x")
                else:
                    ADDRESSES[lable] = hex(location).removeprefix("0x")
            elif sections[0] == 'ORG':
                location = int(sections[1], 16) - 1
            elif sections[0] == 'END':
                #  begin second step of assemble
                lines2 = lines
                location2 = 0
                org = 0
                output = dict()
                for l2 in lines2:
                    sections2 = l2.split()
                    instruction = sections2[0]
                    if len(sections2) == 1:
                        # only RI instructins or END
                        if instruction in src.statics.RI:
                            output[location2] = int(src.statics.RI[instruction])
                        elif instruction == 'END':
                            # write to output file
                            with open("./output/output.asm", "w") as out_file:
                                for key in output.keys():
                                    out_file.write(str(hex(key)) + "\t-->\t" + str(output[key]) + "\n")
                        else:
                            print('facing with error')
                            break
                    elif len(sections2) == 2:
                        if instruction in src.statics.MI:
                            if sections2[1] not in ADDRESSES:
                                print('variable not defind')
                            else:
                                # update warning
                                output[location2] = hex(int(src.statics.MI[instruction][0] + ADDRESSES[sections2[1]], 16)).removeprefix("0x")
                        elif instruction == 'ORG':
                            location2 = int(sections2[1], 16) - 1
                            org = location2
                        elif instruction == 'DEC' or instruction == 'HEX':
                            if sections2[0] == 'HEX':
                                temp = hex(int(sections2[1], 16)).replace("0x", "")
                                while len(temp) < 4:
                                    temp = "0" + temp
                                hex_code = temp
                            else:
                                temp2 = hex(int(sections2[1])).removeprefix("0x").replace("0x", "")
                                while len(temp2) < 4:
                                    temp2 = "0" + temp2
                                hex_code = temp2
                            output[location2] = hex_code
                        elif instruction[-1] == ',':
                            output[location2] = int(src.statics.RI[sections2[1]])
                        else:
                            print('eroor')
                    elif len(sections2) == 3:
                        if sections2[2] == 'I':
                            hex_code = hex(int(src.statics.MI[instruction][1] + ADDRESSES[sections2[1]], 16)).removeprefix("0x")
                        elif sections2[1]  in src.statics.MI:
                            hex_code = hex(int(src.statics.MI[sections2[1]][0] + ADDRESSES[sections2[2]], 16)).removeprefix("0x")
                        else:
                            if sections2[1] == 'HEX':
                                temp = hex(int(sections2[2], 16)).replace("0x", "")
                                while len(temp) < 4:
                                    temp = "0" + temp
                                hex_code = temp
                            else:
                                temp2 = hex(int(sections2[2])).removeprefix("0x").replace("0x", "")
                                while len(temp2) < 4:
                                    temp2 = "0" + temp2
                                hex_code = temp2
                        output[location2] = hex_code
                    elif len(sections2) == 4:
                        hex_code = hex(int(src.statics.MI[sections2[1]] + ADDRESSES[sections2[2]], 16)).removeprefix("0x")
                        output[location2] = hex_code
                    location2 += 1
            location += 1
