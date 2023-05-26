from django.utils.cache import patch_cache_control


def my_cache_control_middleware(next):

    def core_middleware(request):
        response = next(request)
        patch_cache_control(response, max_age=0, no_cache=True)

        return response
    return core_middleware
