"""
Copyright 2019 Skytap Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License."""

# this tool is designed to generate VIP names based on the spec documented here:
# https://confluence.corp.skytap.com/display/INFRA/Host+naming+scheme

if __name__ == '__main__':

    func = ['dory', 'shoal', 'flipper']
    locations = {
        'JNG': {
            'domain': 'skytap-dev.net',
            'environments': {

                4:  {
                  'regions': {
                      'm1': {'subdomain_prefix': None}
                  },
                    'name': 'jenga'
                
                }
            }
        },
        'TUK': {
            'domain': 'skytap.com',
            'environments': {
                1: {
                    'regions': {
                        'm1': {'subdomain_prefix': None},
                    },
                    'name': 'prod',
                },
                5: {
                    'regions': {
                        'm1': {'subdomain_prefix': 'mgt'},
                    },
                   'name': 'integ',
                },
                6: {
                    'regions': {
                        'm1': {'subdomain_prefix': 'mgt'},
                    },
                    'name': 'test',
                }
            }
        }
    }

    fqdns = []
    for F in func:
        for L, subL in locations.iteritems():
            for E, subE in subL['environments'].iteritems():
               for R, subR in subE['regions'].iteritems():

                    subdomain = "{}.{}".format(subE['name'], subL['domain'])

                    subdomain_prefix = subR['subdomain_prefix']
                    if subdomain_prefix:
                        subdomain = "{}.{}".format(subdomain_prefix, subdomain)

                    hostname = '{}{}{}{}1'.format(L, E, R, F)

                    fqdn = '{}.{}'.format(hostname, subdomain)

                    fqdn = fqdn.lower()

                    fqdns.append(fqdn)

    print fqdns