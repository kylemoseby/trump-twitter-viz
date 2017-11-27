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
#
import json
import webapp2

class TrumpHandler(webapp2.RequestHandler):
    def get(self):
        print self
        with open('twitter_user_trumpsAlert.json') as json_file:

            data = json.load(json_file)

            self.response.headers['Content-Type'] = 'application/json'

            self.response.write(json.dumps(data))

app = webapp2.WSGIApplication([
    ('/userinfotrumps', TrumpHandler),
], debug=True)
