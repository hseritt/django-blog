"""Util module for all use with all applications
"""

def get_http_referer(request):
    http_referer = ''
    if 'HTTP_REFERER' in request.META:
        http_referer = request.META['HTTP_REFERER']
    return http_referer
