addHandler('transform', (request, context) => {
    function isValidInput(data) {
        if (data === undefined || data === null) {
            throw new Error("Invalid input: data is undefined or null");
        }
        return true;
    }

    function isValidCode(given_code) {
        if (given_code === undefined || given_code === null) {
            throw new Error("Invalid code: code has no value");
        }
        const code_regex = /^.{1,32}$/;
        if (!code_regex.test(given_code)) {
            throw new Error("Invalid code: " + given_code);
        }
        return true;
    }

    function isValidUserId(given_state) {
        if (given_state === undefined || given_state === null) {
            throw new Error("Invalid user ID: state has no value");
        }
        const state_regex = /^\d{18}$/;
        if (!state_regex.test(given_state)) {
            throw new Error("Invalid user ID: " + given_state);
        }
        return true;
    }

    function getUnixTimestamp() {
        const currentUnixTimestamp = Math.floor(Date.now() / 1000);
        if (isNaN(currentUnixTimestamp)) {
            throw new Error("Failed to generate timestamp");
        }
        return currentUnixTimestamp;
    }

    isValidInput(request.parsed_query);

    const code = request.parsed_query["code"];
    const state = request.parsed_query["state"];

    isValidCode(code);
    isValidUserId(state);

    console.log("Data is okay");

    const time = getUnixTimestamp();

    const payload = { code, state, time };
    const body = { content: JSON.stringify(payload) };

    const updatedRequest = { ...request, body };
    updatedRequest.headers['content-type'] = 'application/json';
    delete updatedRequest.query;

    return updatedRequest;
});
