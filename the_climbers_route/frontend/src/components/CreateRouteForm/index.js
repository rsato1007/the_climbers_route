import React from "react";
import CreateRoutePage from "../../pages/CreateRoutePage";

const CreateRouteForm = ({ name, setName, description, setDescription, location, setLocation, difficulty, setDifficulty, image, setImage, climb_type, setType, pitch, setPitch }) => {
    const submitForm = async () => {
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                name,
                description,
                location,
                difficulty,
                image,
                climb_type,
                pitch
            }),
        };
        fetch('/api/route/new', requestOptions)
        .then((res) => res.json())
        .then((data) => console.log(data));
    }

    return (
        <div>
            <input
                type="text"
                value={name}
                onChange={e => setName(e.target.value)}
                title="name"
                placeholder="E.g., Colorado Route"
            />
            <input
                type="textarea"
                value={description}
                onChange={e => setDescription(e.target.value)}
                title="description"
            />
            <input
                type="text"
                value={location}
                onChange={e => setLocation(e.target.value)}
                title="location"
                placeholder="E.g., Englewood, Colorado"
            />
            <input 
                type="number"
                value={difficulty}
                onChange={e => setDifficulty(e.target.value)}
                title="difficulty"
                placeholder="E.g., 5.11"
                min="5.1"
                max="6.0"
            />
            <input
                type="file"
                onChange={e => setImage(e.target.value)}
                accept="image/png, image.jpeg"
                title="image"
            />
            <select 
                name="climb_type" 
                onChange={e => setType(e.target.value)}
            >
                <option value='' selected disabled hidden>Choose Here</option>
                <option value="Ice">Ice</option>
                <option value="Rock">Rock</option>
                <option value="Mixed">Mixed</option>
            </select>
            <input 
                type="number"
                value={pitch}
                onChange={e => setPitch(e.target.value)}
                title="pitch"
                placeholder="E.g., 5 pitches"
                min="0"
                max="10"
            />
            <button onClick={submitForm}>Submit Form</button>
        </div>
    )
}

export default CreateRouteForm;