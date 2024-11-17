"use client"
import { useState } from "react";
import Block from "./block";

export default function Hoverable() {
  const [blocks, setBlocks] = useState([{ id: 1 }]);

  const addBlock = (id: number) => {
    const newBlock = { id: blocks.length + 1 };
    const index = blocks.findIndex((block) => block.id === id) + 1;
    const updatedBlocks = [...blocks];
    updatedBlocks.splice(index, 0, newBlock);
    setBlocks(updatedBlocks);
  };

  return (
    <div className="p-6">
      {blocks.map((block) => (
        <Block key={block.id} id={block.id} onAddBlock={addBlock} />
      ))}
    </div>
  );
}
