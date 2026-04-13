import React, {
  type ElementType,
  type ReactNode,
  useContext,
  useEffect,
  useRef,
} from 'react';
import { CSSTransition as ReactCSSTransition } from 'react-transition-group';

type TransitionContextType = {
  parent: {
    show?: boolean;
    appear?: boolean;
    isInitialRender?: boolean;
  };
};

const TransitionContext = React.createContext<TransitionContextType>({
  parent: {},
});

function useIsInitialRender(): boolean {
  const isInitialRender = useRef(true);

  useEffect(() => {
    isInitialRender.current = false;
  }, []);

  return isInitialRender.current;
}

type CSSTransitionProps = {
  show?: boolean;
  enter?: string;
  enterStart?: string;
  enterEnd?: string;
  leave?: string;
  leaveStart?: string;
  leaveEnd?: string;
  appear?: boolean;
  unmountOnExit?: boolean;
  tag?: ElementType;
  children?: ReactNode;
} & React.HTMLAttributes<HTMLElement>;

function CSSTransition({
  show,
  enter = '',
  enterStart = '',
  enterEnd = '',
  leave = '',
  leaveStart = '',
  leaveEnd = '',
  appear,
  unmountOnExit,
  tag = 'div',
  children,
  ...rest
}: CSSTransitionProps) {
  const enterClasses = enter.split(' ').filter(Boolean);
  const enterStartClasses = enterStart.split(' ').filter(Boolean);
  const enterEndClasses = enterEnd.split(' ').filter(Boolean);
  const leaveClasses = leave.split(' ').filter(Boolean);
  const leaveStartClasses = leaveStart.split(' ').filter(Boolean);
  const leaveEndClasses = leaveEnd.split(' ').filter(Boolean);

  const removeFromDom = unmountOnExit;
  const nodeRef = useRef<HTMLElement | null>(null);
  const Component = tag;
  const addClasses = (node: HTMLElement, classes: string[]): void => {
    if (classes.length > 0) {
      node.classList.add(...classes);
    }
  };

  const removeClasses = (
    node: HTMLElement,
    classes: string[],
  ): void => {
    if (classes.length > 0) {
      node.classList.remove(...classes);
    }
  };

  return (
    <ReactCSSTransition
      appear={appear}
      nodeRef={nodeRef}
      unmountOnExit={removeFromDom}
      in={show}
      addEndListener={(done) => {
        const node = nodeRef.current;
        if (!node) return;
        node.addEventListener('transitionend', done, false);
      }}
      onEnter={() => {
        const node = nodeRef.current;
        if (!node) return;

        if (!removeFromDom) node.style.display = '';

        addClasses(node, [...enterClasses, ...enterStartClasses]);
      }}
      onEntering={() => {
        const node = nodeRef.current;
        if (!node) return;

        removeClasses(node, enterStartClasses);
        addClasses(node, enterEndClasses);
      }}
      onEntered={() => {
        const node = nodeRef.current;
        if (!node) return;

        removeClasses(node, [...enterEndClasses, ...enterClasses]);
      }}
      onExit={() => {
        const node = nodeRef.current;
        if (!node) return;

        addClasses(node, [...leaveClasses, ...leaveStartClasses]);
      }}
      onExiting={() => {
        const node = nodeRef.current;
        if (!node) return;

        removeClasses(node, leaveStartClasses);
        addClasses(node, leaveEndClasses);
      }}
      onExited={() => {
        const node = nodeRef.current;
        if (!node) return;

        removeClasses(node, [...leaveEndClasses, ...leaveClasses]);

        if (!removeFromDom) node.style.display = 'none';
      }}
    >
      <Component
        ref={nodeRef}
        {...rest}
        style={{
          display: !removeFromDom ? 'none' : undefined,
          ...(rest.style || {}),
        }}
      >
        {children}
      </Component>
    </ReactCSSTransition>
  );
}

type BaseTransitionProps = {
  show?: boolean;
  appear?: boolean;
  enter?: string;
  enterStart?: string;
  enterEnd?: string;
  leave?: string;
  leaveStart?: string;
  leaveEnd?: string;
  unmountOnExit?: boolean;
  tag?: React.ElementType;
  children?: React.ReactNode;
};

type TransitionProps<T extends React.ElementType = 'div'> = {
  tag?: T;
} & BaseTransitionProps &
  Omit<React.ComponentPropsWithoutRef<T>, keyof BaseTransitionProps>;

function Transition<T extends React.ElementType = 'div'>(
  props: TransitionProps<T>,
) {
  const {
    tag: Tag = 'div',
    show,
    appear,
    enter,
    enterStart,
    enterEnd,
    leave,
    leaveStart,
    leaveEnd,
    unmountOnExit,
    ...rest
  } = props;
  const { parent } = useContext(TransitionContext);
  const isInitialRender = useIsInitialRender();
  const isChild = show === undefined;

  if (isChild) {
    return (
      <CSSTransition
        appear={parent.appear || !parent.isInitialRender}
        show={parent.show}
        {...rest}
      />
    );
  }

  return (
    <TransitionContext.Provider
      value={{
        parent: {
          show,
          isInitialRender,
          appear,
        },
      }}
    >
      <CSSTransition appear={appear} show={show} {...rest} />
    </TransitionContext.Provider>
  );
}

export default Transition;
