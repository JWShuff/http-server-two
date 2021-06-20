class Request:
    def __init__(self, request_text):
        self.parse_request(request_text.recv(4096).decode('utf-8').split('\r\n'))

    def parse_request(self, decoded_request_text):
        self.parsed_request = {}
        self.parsed_request['uri'] = decoded_request_text.pop(
            0).replace("GET ", "").replace(" HTTP/1.1", "")
        for item in decoded_request_text:
            if item == "":
                continue
            split_item = item.split(': ')
            self.parsed_request[split_item[0]] = split_item[1]

    #   self.parsed_request = {
    #     'method': request_as_list[0].split(' ')[0],
    #     'uri': request_as_list[0].split(' ')[1],
    #   }
    #   for row in request_as_list[1:-2]:
    #     if row == "":
    #         continue
    #     split_list = row.split(': ')
    #     self.parsed_request[split_list[0]] = split_list[1]
