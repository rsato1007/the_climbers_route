import React, { useEffect, useState } from "react";
import CreateRouteForm from "../../components/CreateRouteForm";

const CreateRoutePage = () => {
    const [name, setName] = useState("");
    const [description, setDescription] = useState("")
    const [location, setLocation] = useState("");
    const [difficulty, setDifficulty] = useState("");
    const [image, setImage] = useState("");
    const [climb_type, setType] = useState("");
    const [pitch, setPitch] = useState("");

    return (
        <div>
            <CreateRouteForm 
                name={name}
                setName={setName}
                description={description}
                setDescription={setDescription}
                location={location}
                setLocation={setLocation}
                difficulty={difficulty}
                setDifficulty={setDifficulty}
                image={image}
                setImage={setImage}
                climb_type={climb_type}
                setType={setType}
                pitch={pitch}
                setPitch={setPitch}
            />
        </div>
    )
}

export default CreateRoutePage;