#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2
import caesar
import cgi

#import caesar
html_str="""
<!DOCTYPE html>
<html>
<body>
<form method="post">
    rotation amount:<input name="submit"type="submit" value="submit">
                    <input name="rotate" type="text" value="">
    word:           <input name="word" type="text" value="">
</form>
</body>
</html>"""
class MainHandler(webapp2.RequestHandler):
    def get(self):


        self.response.write(html_str)


    def post(self):
        rotate=self.request.get("rotate")
        word=self.request.get("word")
        rotate_character = caesar.encrypted(word,int(rotate))
        response = html_str


        self.response.write(rotate_character)



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
