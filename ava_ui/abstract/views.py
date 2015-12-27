



class ObjectIndex(generic.TemplateView):
    url = settings.API_BASE_URL + '/organize/person/'

    def get(self, request):
        log.debug(str(self.__class__) + " GET called")
        log.debug(str(self.__class__) + " GET attempting to get data from url " + self.url)
        header = {'Authorization': 'JWT ' + TOKEN}
        log.debug(str(self.__class__) + " GET header = " + str(header))
        results = requests.get(self.url, headers=header)
        if results.status_code is '200':
            # log.debug(str(self.__class__) + " GET results = " + str(results))
            people = results.json()
            person_list = {'people': people['results']}
            # log.debug(str(self.__class__) + " GET attemting to render " + str(person_list))
            return render(request, 'organize/person/person_index.html', context=person_list)
        else:
            return handle_error(request, results.status_code)


class ObjectDetail(generic.TemplateView):
    url = settings.API_BASE_URL + '/organize/person/%(number)06d/'

    def get(self, request, **kwargs):
        log.debug(str(self.__class__) + " GET called")
        pk = self.kwargs.get('pk')
        url = self.url % {"number": pk}
        log.debug(str(self.__class__) + " GET attempting to get data from url " + url)

        header = {'Authorization': 'JWT ' + TOKEN}
        log.debug(str(self.__class__) + " GET header = " + str(header))
        log.debug(str(self.__class__) + " GET header = " + str(header))
        results = requests.get(self.url, headers=header)
        if results.status_code is '200':
            log.debug(str(self.__class__) + " GET results = " + str(results))
            people = results.json()
            person = {'people': people['results']}
            log.debug(str(self.__class__) + " GET attemPting to render " + str(person))
            return render(request, 'organize/person/person_detail.html', person)
        else:
            return handle_error(request, results.status_code)