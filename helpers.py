# Helper Methods

import json
import pprint

def show_json(rest_response):
    if (rest_response.code != 200):
        print(rest_response.description)
    if (rest_response.code != 204):
        data = json.decoder(rest_response)  # I feel like this isn't necessary if I'm using requests
        pretty_printer = pprint.PrettyPrinter(indent = 4)
        assert isinstance(data, object)
        pretty_printer.pprint(data)

# FIXME: This is the Ruby implementation

# def show_json(rest_response)
#   puts rest_response.description unless rest_response.code == 200
#   if rest_response.code != 204
#     data = parse_json rest_response
#     puts JSON.pretty_generate(data, {indent: '    '}) unless data.nil?
#   end
# end
#
# def parse_json(rest_response)
#   json = rest_response.to_s
#   begin
#     data = JSON.parse json
#   rescue JSON::ParserError => e
#     puts 'Invalid JSON response'
#     nil
#   end
# end

