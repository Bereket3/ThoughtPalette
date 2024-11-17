import { useState } from "react";
import dynamic from "next/dynamic";
import "react-quill/dist/quill.snow.css"; // Quill styles

const ReactQuill = dynamic(() => import("react-quill"), { ssr: false });

export default function Block({ id, onAddBlock }: {
  id: number,
  onAddBlock: Function
}) {
  const [isHovered, setIsHovered] = useState(false);
  const [content, setContent] = useState("");

  return (
    <div
      className="relative w-full bg-gray-100 dark:bg-gray-600 p-4 rounded-md shadow-sm my-4"
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => setIsHovered(false)}
    >
      <ReactQuill
        value={content}
        theme="snow"
        onChange={setContent}
        placeholder="Type your content here..."
        className="bg-white dark:bg-black border rounded-md"
      />

      {isHovered && (
        <>
          <button
            className="absolute -bottom- right-1/2 transform -translate-x-1/2 bg-blue-500 text-white px-3 py-1 rounded-full shadow hover:bg-blue-600"
            onClick={() => onAddBlock(id)}
          >
            Text
          </button>
          <button
            className="absolute -bottom-4 left-1/2 transform -translate-x-1/2 bg-blue-500 text-white px-3 py-1 rounded-full shadow hover:bg-blue-600">
            File
          </button>
        </>

      )}
    </div>
  );
}
