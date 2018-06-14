#

class API ():
    """
    Letterboxd API helpers
    """

    def api(self, path, params = {}, form = None, headers = {}, method = "get"):
        """
        :param path: The endpoint for the service
        :param params:
        :param form:
        :param headers:
        :param method: HTML methods get, post, put, patch
        :return: 
        """

        if (form):
            pass



### Ruby implementation
#
# def api(path, params: {}, form: nil, headers: {: accept => "application/json", "Content-Type" = > "application/json"}, method: "get")
#     headers["Authorization"] = "Bearer #{@token}" unless @ token.nil?
#     url = add_metadata "#{@api_base}/#{path}"
#     if form
#         body = URI.encode_www_form form
#         headers["Content-Type"] = "application/x-www-form-urlencoded"
#         signature = sign method.upcase, url, body
#         headers["Authorization"] = "Signature #{signature}"
#     elsif
#         method.downcase = ~ / (post | put | patch) /
#         body = JSON.generate remove_nil_params(params)
#         signature = sign method.upcase, url, body
#         url = add_params(url, {:signature = > signature})
#     else
#         body = ""
#         url = add_params(url, params)
#         signature = sign method.upcase, url
#         url = add_params(url, {:signature = > signature})
#     end
#     begin
#         RestClient.proxy = CHARLES_PROXY
#         rest_call method, url, body, headers
#     rescue Errno::ECONNREFUSED
#         RestClient.proxy = nil
#         rest_call method, url, body, headers
#     end
# end
