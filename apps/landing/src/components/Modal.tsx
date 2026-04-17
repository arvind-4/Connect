import { type ReactNode, useEffect, useRef } from "react";

import Transition from "./Transition";

type ModalProps = {
  children?: ReactNode;
  id?: string;
  ariaLabel?: string;
  show: boolean;
  handleClose: () => void;
};

export default function Modal({
  children,
  id,
  ariaLabel,
  show,
  handleClose,
}: ModalProps): JSX.Element {
  const modalContent = useRef<HTMLDivElement | null>(null);

  useEffect((): (() => void) => {
    const clickHandler = (event: MouseEvent): void => {
      if (
        show === false ||
        modalContent.current === null ||
        modalContent.current.contains(event.target as Node)
      ) {
        return;
      }
      handleClose();
    };

    document.addEventListener("click", clickHandler);

    return (): void => {
      document.removeEventListener("click", clickHandler);
    };
  }, [show, handleClose]);

  useEffect((): (() => void) => {
    const keyHandler = (event: KeyboardEvent): void => {
      if (event.key !== "Escape") return;
      handleClose();
    };

    document.addEventListener("keydown", keyHandler);

    return (): void => {
      document.removeEventListener("keydown", keyHandler);
    };
  }, [handleClose]);

  return (
    <>
      <Transition
        id={`${id}-overlay`}
        className="fixed inset-0 z-50 bg-white bg-opacity-75 transition-opacity backdrop-blur-sm"
        show={show}
        enter="transition ease-out duration-200"
        enterStart="opacity-0"
        enterEnd="opacity-100"
        leave="transition ease-out duration-100"
        leaveStart="opacity-100"
        leaveEnd="opacity-0"
        aria-hidden="true"
      />

      <Transition
        id={`${id}-content`}
        className="fixed inset-0 z-50 overflow-hidden flex items-center justify-center transform px-4 sm:px-6"
        role="dialog"
        aria-modal="true"
        aria-labelledby={ariaLabel}
        show={show}
        enter="transition ease-out duration-200"
        enterStart="opacity-0 scale-95"
        enterEnd="opacity-100 scale-100"
        leave="transition ease-out duration-200"
        leaveStart="opacity-100 scale-100"
        leaveEnd="opacity-0 scale-95"
      >
        <div className="bg-white overflow-auto max-w-6xl w-full max-h-full" ref={modalContent}>
          {children}
        </div>
      </Transition>
    </>
  );
}
