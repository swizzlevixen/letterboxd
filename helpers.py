"""
Helper Methods for JSON responses
TODO: See if this is really necessary if I'm using `requests`. I feel like a lot of this is already taken care of.
"""

import json

def show_json(rest_response):
    if (rest_response.code != 200):
        print(rest_response.description)
    if (rest_response.code != 204):
        print json.dumps(rest_response, indent = 4, sort_keys = True)

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

