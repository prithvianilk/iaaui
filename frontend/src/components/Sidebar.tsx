import { useState } from "react";

export type NodeMeta = {
  nodeType: "input" | "output";
  label: string;
};

type SidebarProps = {
  submit: () => void;
};

const Sidebar = ({ submit }: SidebarProps) => {
  const onDragStart = (event: any, data: NodeMeta, type: string) => {
    event.dataTransfer.setData("label", data.label);
    event.dataTransfer.setData("type", data.nodeType);
    event.dataTransfer.setData("resourceType", type);
    event.dataTransfer.effectAllowed = "move";
  };

  const [clusterName, setClusterName] = useState("Cluster");
  const [numberOfHosts, setNumberOfHosts] = useState(1);

  return (
    <div className="flex h-full flex-col justify-between px-2 py-5">
      <div>
        <div className="flex flex-col justify-center">
          <div className="mb-2 text-center text-lg">Create a cluster</div>
          <label>Cluster Name</label>
          <input
            value={clusterName}
            type="text"
            placeholder="Cluster"
            onChange={(e) => setClusterName(e.currentTarget.value)}
            className="input my-2 w-full max-w-xs"
          />
          <label>Number of hosts</label>
          <input
            type="text"
            placeholder="1"
            value={numberOfHosts}
            onChange={(e) => {
              try {
                const newNumberOfHosts = Number.parseInt(e.currentTarget.value);
                if (Number.isNaN(newNumberOfHosts)) return;
                setNumberOfHosts(newNumberOfHosts);
              } finally {
              }
            }}
            className="input my-2 w-full max-w-xs"
          />
          <hr className="my-5" />
          <div
            className="node w-full text-lg"
            onDragStart={(event) =>
              // @ts-ignore
              onDragStart(
                event,
                { label: "Cloud Name", nodeType: "input" },
                "cloud"
              )
            }
            draggable
          >
            Cloud
          </div>
          <hr className="my-5" />
          <div
            className="node my-2 w-full text-lg"
            onDragStart={(event) =>
              onDragStart(
                event,
                // @ts-ignore
                {
                  label: "Cluster Name",
                },
                "cluster"
              )
            }
            draggable
          >
            Cluster
          </div>
        </div>
        <hr className="my-5" />
        <div
          className="node w-full text-lg"
          onDragStart={(event) =>
            // @ts-ignore
            onDragStart(
              event,
              {
                label: "App Name",
                nodeType: "output",
              },
              "app"
            )
          }
          draggable
        >
          App
        </div>
        <hr className="my-5" />
        <div
          className="node w-full text-lg"
          onDragStart={(event) =>
            // @ts-ignore
            onDragStart(
              event,
              {
                label: "Database Name",
                nodeType: "output",
              },
              "database"
            )
          }
          draggable
        >
          Database
        </div>
      </div>
      <div className="flex justify-center">
        <button className="btn w-4/5" onClick={submit}>
          Submit
        </button>
      </div>
    </div>
  );
};

export default Sidebar;
