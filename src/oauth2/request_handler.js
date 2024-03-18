addHandler('transform', (request, context) => {

    //functions to validate the args

    function isValidCode(given_code) {
        // check if code is undefined
        if (given_code === undefined || given_code === null) {
            console.warn("code has no value");
            return false;
        }
        return true
    }

    function isValidUserId(given_state) {
        // Check if state is undefined or null
        if (given_state === undefined || given_state === null) {
            console.warn("state has no value");
            return false;
        }

        // check if the string consists of only digits and has a length of 18
        var regex = /^\d{18}$/;
        if (!regex.test(given_state)) {
            console.warn("state is not a valid user id");
            return false
        }
        return true
    }

    function getUnixTimestamp() {
        const currentUnixTimestamp = Math.floor(Date.now() / 1000);
        return currentUnixTimestamp
    }

    // get queries
    const code = request.parsed_query["code"];
    const state = request.parsed_query["state"];

    // check if queries are okay
    if (!isValidCode(code) || !isValidUserId(state)) {
        console.error("Invalid data")
        console.error("code: '" + code + "'")
        console.error("state: '" + state + "'")
        return null
    }
    console.log("data is okay")

    // create a json like str
    const payload = {
        code: code,
        state: state,
        time: getUnixTimestamp()
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
    delete request.query;

    return request;
});
