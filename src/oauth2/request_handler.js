addHandler('transform', (request, context) => {
    // Function to parse query string
    function parseQueryString(queryString) {
        const params = {};
        const queryStringWithoutQuestionMark = queryString.substring(1);
        const queryComponents = queryStringWithoutQuestionMark.split('&');
        for (const component of queryComponents) {
            const [key, value] = component.split('=');
            params[key] = value;
        }
        return params;
    }

    // Parse the query string to extract the value of the "code" parameter
    const queryParams = parseQueryString(request.query);
    const code = queryParams['code'];

    // create a json like str
    const payload = {
        code: code
    };
    const jsonPayload = JSON.stringify(payload);


    // Create the body object with the extracted code
    const body = {
        content: jsonPayload
    };

    // Update the request object with the new body
    request.body = body;
    request.headers['content-type'] = 'application/json';

    // Remove the parsed_query field as it's not needed anymore
    delete request.query

    return request;
});
