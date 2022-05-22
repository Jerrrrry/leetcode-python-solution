def reorder(logs):
        l,d=[],[]

        for log in logs:
                data=log.split(' ')

                if data[1].isdigit():
                        d.append(log)
                else:
                        l.append([' '.join(data[1:]),data[0]])

        l.sort()

        return [x[1]+' '+x[0] for x in l]+d