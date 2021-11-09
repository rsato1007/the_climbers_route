import React from "react";
import CreateRoutePage from "../../pages/CreateRoutePage";

const CreateRouteForm = ({ name, location, difficulty, image, tyope, pitch }) => {
    const submitForm = async () => {
        console.log("Form be submitted bud");
    }

    return (
        <div>
            <button onClick={submitForm}>Submit Form</button>
        </div>
    )
}

export default CreateRouteForm;