import React, { useEffect, useState } from "react";
import CreateRouteForm from "../../components/CreateRouteForm";

const CreateRoutePage = () => {
    const [name, setName] = useState("");
    const [location, setLocation] = useState("");
    const [difficulty, setDifficulty] = useState("");
    const [image, setImage] = useState("");
    const [type, setType] = useState("");
    const [pitch, setPitch] = useState("");

    return (
        <div>
            <CreateRouteForm 
                name={name}
                location={location}
                difficulty={difficulty}
                image={image}
                type={type}
                pitch={pitch}
            />
        </div>
    )
}

export default CreateRoutePage;