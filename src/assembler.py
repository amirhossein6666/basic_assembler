import src.statics
ADDRESSES = dict()


def assemble(in_file):
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
                output = dict()
                for l2 in lines2:
                    sections2 = l2.split()
                    instruction = sections2[0]
                    if len(sections2) == 1:
                        if instruction == 'END':
                            keys = list(output.keys()).sort()
                            for key in keys:
                                output[key] = struct.pack('>i', int(output[key], 16))
                            # right to output file 
                        elif instruction in src.statics.RI:
                            output[location2] = hex(src.statics.RI[instruction])
                        else:
                            print('facing with error')
                            break
                    

            location += 1
