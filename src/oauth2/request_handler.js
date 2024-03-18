addHandler('transform', (request, context) => {
    // get code query
    const code = request.parsed_query["code"]
    if (code === undefined) {
        console.error("Code is undefined")
        return null
    }
    console.log(code)

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
