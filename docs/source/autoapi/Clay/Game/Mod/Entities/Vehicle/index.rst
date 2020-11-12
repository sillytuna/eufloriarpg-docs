
Vehicle Class
=============



Namespace
    :dn:ns:`Clay.Game.Mod.Entities`

Assemblies
    * Clay.Game

----

.. contents::
   :local:



Inheritance Hierarchy
---------------------

* :dn:cls:`System.Object`
* :dn:cls:`Tuna.Mob`
* :dn:cls:`Clay.Game.Mod.Entities.Entity`
* :dn:cls:`Clay.Game.Mod.Entities.Vehicle`




Syntax
------

.. code-block:: csharp

    public class Vehicle : Entity, IComparable, IAudioSourceInfo, ITargettable, IPathFindingAgent





.. dn:class:: Clay.Game.Mod.Entities.Vehicle
    :hidden:

.. dn:class:: Clay.Game.Mod.Entities.Vehicle


Constructors
------------

.. dn:class:: Clay.Game.Mod.Entities.Vehicle
    :noindex:
    :hidden:

    .. dn:constructor:: Clay.Game.Mod.Entities.Vehicle.Vehicle()




        .. code-block:: csharp

            public Vehicle()



Properties
----------

.. dn:class:: Clay.Game.Mod.Entities.Vehicle
    :noindex:
    :hidden:

    .. dn:property:: Clay.Game.Mod.Entities.Vehicle.PathEndPoint



        :rtype: UnityEngine.Vector2

        .. code-block:: csharp

            public Vector2 PathEndPoint { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vehicle.PathStartPoint



        :rtype: UnityEngine.Vector2

        .. code-block:: csharp

            public Vector2 PathStartPoint { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vehicle._behaviour



        :rtype: System.String

        .. code-block:: csharp

            public string _behaviour { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vehicle._canReverse



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool _canReverse { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vehicle._drag



        :rtype: System.Single

        .. code-block:: csharp

            public float _drag { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vehicle._goHomeness



        :rtype: System.Single

        .. code-block:: csharp

            public float _goHomeness { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vehicle._maxAcceleration



        :rtype: System.Single

        .. code-block:: csharp

            public float _maxAcceleration { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vehicle._offsetFromOwner



        :rtype: UnityEngine.Vector2

        .. code-block:: csharp

            public Vector2 _offsetFromOwner { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vehicle._pitchSpeed



        :rtype: System.Single

        .. code-block:: csharp

            public float _pitchSpeed { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vehicle._pitchSpeedFollowMultiplier



        :rtype: System.Single

        .. code-block:: csharp

            public float _pitchSpeedFollowMultiplier { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vehicle._targetBehaviour



        :rtype: System.String

        .. code-block:: csharp

            public string _targetBehaviour { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vehicle._vehicleHandling



        :rtype: System.String

        .. code-block:: csharp

            public string _vehicleHandling { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vehicle.avoidanceBraking



        :rtype: System.Single

        .. code-block:: csharp

            public static float avoidanceBraking { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vehicle.behavioursEnabled



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool behavioursEnabled { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vehicle.brakeIfSpeedRatioGreaterThan



        :rtype: System.Single

        .. code-block:: csharp

            public static float brakeIfSpeedRatioGreaterThan { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vehicle.braking



        :rtype: System.Single

        .. code-block:: csharp

            public static float braking { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vehicle.defaultMaxSpeed



        :rtype: System.Single

        .. code-block:: csharp

            public float defaultMaxSpeed { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Vehicle.goHomeness



        :rtype: System.Single

        .. code-block:: csharp

            public float goHomeness { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Vehicle.isInAvoidanceMode



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isInAvoidanceMode { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Vehicle.lastSpeed



        :rtype: System.Single

        .. code-block:: csharp

            public float lastSpeed { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Vehicle.maxSpeedDampingTime



        :rtype: System.Single

        .. code-block:: csharp

            public static float maxSpeedDampingTime { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vehicle.pitch



        :rtype: System.Single

        .. code-block:: csharp

            public override float pitch { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Vehicle.requestForceUpdate



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool requestForceUpdate { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vehicle.speed



        :rtype: System.Single

        .. code-block:: csharp

            public override float speed { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Vehicle.steeringData



        :rtype: AISteerCalcData

        .. code-block:: csharp

            public AISteerCalcData steeringData { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Vehicle.targetMaxSpeed



        :rtype: System.Single

        .. code-block:: csharp

            public float targetMaxSpeed { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Vehicle.targetSteering



        :rtype: AISteerTarget

        .. code-block:: csharp

            public AISteerTarget targetSteering { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Vehicle.trackingPosition



        :rtype: System.Nullable<System.Nullable`1>{UnityEngine.Vector3<UnityEngine.Vector3>}

        .. code-block:: csharp

            public Vector3? trackingPosition { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vehicle.useVehiclePhysics



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool useVehiclePhysics { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vehicle.visiblePitch



        :rtype: System.Single

        .. code-block:: csharp

            public override float visiblePitch { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Vehicle.visiblePitchNormalRotationTime



        :rtype: System.Single

        .. code-block:: csharp

            public static float visiblePitchNormalRotationTime { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vehicle.visiblePitchSlowRotationAngle



        :rtype: System.Single

        .. code-block:: csharp

            public static float visiblePitchSlowRotationAngle { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Vehicle.visiblePitchSlowRotationTime



        :rtype: System.Single

        .. code-block:: csharp

            public static float visiblePitchSlowRotationTime { get; set; }



Fields
------

.. dn:class:: Clay.Game.Mod.Entities.Vehicle
    :noindex:
    :hidden:

    .. dn:field:: Clay.Game.Mod.Entities.Vehicle.MIN_FORCE_MAGNITUDE



        :rtype: System.Single

        .. code-block:: csharp

            public const float MIN_FORCE_MAGNITUDE = 0.025F

    .. dn:field:: Clay.Game.Mod.Entities.Vehicle._preferredTarget



        :rtype: Clay.Game.Mod.Entities.Entity

        .. code-block:: csharp

            public Entity _preferredTarget

    .. dn:field:: Clay.Game.Mod.Entities.Vehicle.mAcceleration



        :rtype: UnityEngine.Vector2

        .. code-block:: csharp

            protected Vector2 mAcceleration

    .. dn:field:: Clay.Game.Mod.Entities.Vehicle.mDefaultMaxSpeed



        :rtype: System.Single

        .. code-block:: csharp

            protected float mDefaultMaxSpeed

    .. dn:field:: Clay.Game.Mod.Entities.Vehicle.mDrag



        :rtype: System.Single

        .. code-block:: csharp

            protected float mDrag

    .. dn:field:: Clay.Game.Mod.Entities.Vehicle.mForceAngle



        :rtype: System.Single

        .. code-block:: csharp

            public float mForceAngle

    .. dn:field:: Clay.Game.Mod.Entities.Vehicle.mForceMagnitude



        :rtype: System.Single

        .. code-block:: csharp

            public float mForceMagnitude

    .. dn:field:: Clay.Game.Mod.Entities.Vehicle.mIsForceCalculationRequired



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool mIsForceCalculationRequired

    .. dn:field:: Clay.Game.Mod.Entities.Vehicle.mMaxAcceleration



        :rtype: System.Single

        .. code-block:: csharp

            public float mMaxAcceleration

    .. dn:field:: Clay.Game.Mod.Entities.Vehicle.mPitch



        :rtype: System.Single

        .. code-block:: csharp

            public float mPitch

    .. dn:field:: Clay.Game.Mod.Entities.Vehicle.mPitchInterpolator



        :rtype: System.Single

        .. code-block:: csharp

            public float mPitchInterpolator

    .. dn:field:: Clay.Game.Mod.Entities.Vehicle.mPitchSpeed



        :rtype: System.Single

        .. code-block:: csharp

            public float mPitchSpeed

    .. dn:field:: Clay.Game.Mod.Entities.Vehicle.mSpeed



        :rtype: System.Single

        .. code-block:: csharp

            public float mSpeed

    .. dn:field:: Clay.Game.Mod.Entities.Vehicle.mTargetMaxSpeed



        :rtype: System.Single

        .. code-block:: csharp

            protected float mTargetMaxSpeed

    .. dn:field:: Clay.Game.Mod.Entities.Vehicle.mVisiblePitch



        :rtype: System.Single

        .. code-block:: csharp

            protected float mVisiblePitch



Methods
-------

.. dn:class:: Clay.Game.Mod.Entities.Vehicle
    :noindex:
    :hidden:

    .. dn:method:: Clay.Game.Mod.Entities.Vehicle.Activate(Attributes, UnityEngine.Vector2, System.Single, Colony, Team)



        :type attr: Attributes

        :type atPosition: UnityEngine.Vector2

        :type atAngle: System.Single

        :type colony: Colony

        :type newTeam: Team


        .. code-block:: csharp

            public override void Activate(Attributes attr, Vector2 atPosition, float atAngle, Colony colony, Team newTeam)

    .. dn:method:: Clay.Game.Mod.Entities.Vehicle.CalculateCachedForce()




        .. code-block:: csharp

            public void CalculateCachedForce()

    .. dn:method:: Clay.Game.Mod.Entities.Vehicle.CalculateForce()




        .. code-block:: csharp

            public void CalculateForce()

    .. dn:method:: Clay.Game.Mod.Entities.Vehicle.CleanUpLevel()




        .. code-block:: csharp

            public static void CleanUpLevel()

    .. dn:method:: Clay.Game.Mod.Entities.Vehicle.CloneConfiguration(Tuna.Mob)



        :type mob: Tuna.Mob


        .. code-block:: csharp

            public override void CloneConfiguration(Mob mob)

    .. dn:method:: Clay.Game.Mod.Entities.Vehicle.Die(System.Boolean, System.Boolean, System.Boolean)



        :type exploded: System.Boolean

        :type trash: System.Boolean

        :type quietly: System.Boolean


        .. code-block:: csharp

            public override void Die(bool exploded = false, bool trash = true, bool quietly = false)

    .. dn:method:: Clay.Game.Mod.Entities.Vehicle.DoPhysics(System.Single)



        :type time: System.Single


        .. code-block:: csharp

            public override void DoPhysics(float time)

    .. dn:method:: Clay.Game.Mod.Entities.Vehicle.DoorCollisionHandler(Door)



        :type door: Door


        .. code-block:: csharp

            public override void DoorCollisionHandler(Door door)

    .. dn:method:: Clay.Game.Mod.Entities.Vehicle.EntityFixedUpdate(System.Single)



        :type time: System.Single


        .. code-block:: csharp

            public override void EntityFixedUpdate(float time)

    .. dn:method:: Clay.Game.Mod.Entities.Vehicle.FixedUpdateAllVehicleForces(System.Single, System.Int32, System.Int32)



        :type time: System.Single

        :type thread: System.Int32

        :type threadCount: System.Int32


        .. code-block:: csharp

            public static void FixedUpdateAllVehicleForces(float time, int thread, int threadCount)

    .. dn:method:: Clay.Game.Mod.Entities.Vehicle.ForceSpeedImmediately(System.Single)



        :type value: System.Single


        .. code-block:: csharp

            public void ForceSpeedImmediately(float value)

    .. dn:method:: Clay.Game.Mod.Entities.Vehicle.GenerateCharacteristics()




        .. code-block:: csharp

            protected override void GenerateCharacteristics()

    .. dn:method:: Clay.Game.Mod.Entities.Vehicle.GenerateDependantCharacteristics()




        .. code-block:: csharp

            protected override void GenerateDependantCharacteristics()

    .. dn:method:: Clay.Game.Mod.Entities.Vehicle.GivePathData(System.Collections.Generic.IList<UnityEngine.Vector3>)



        :type path: System.Collections.Generic.IList<System.Collections.Generic.IList`1>{UnityEngine.Vector3<UnityEngine.Vector3>}


        .. code-block:: csharp

            public void GivePathData(IList<Vector3> path)

    .. dn:method:: Clay.Game.Mod.Entities.Vehicle.InitialiseApp()




        .. code-block:: csharp

            public static void InitialiseApp()

    .. dn:method:: Clay.Game.Mod.Entities.Vehicle.InitialiseLevel()




        .. code-block:: csharp

            public static void InitialiseLevel()

    .. dn:method:: Clay.Game.Mod.Entities.Vehicle.ReadAIStateConfig(AIState)



        :type state: AIState


        .. code-block:: csharp

            public override void ReadAIStateConfig(AIState state)

    .. dn:method:: Clay.Game.Mod.Entities.Vehicle.RebuildBehaviours()




        .. code-block:: csharp

            public void RebuildBehaviours()

    .. dn:method:: Clay.Game.Mod.Entities.Vehicle.RebuildPrototype()




        .. code-block:: csharp

            public override void RebuildPrototype()

    .. dn:method:: Clay.Game.Mod.Entities.Vehicle.RenderDebug()




        .. code-block:: csharp

            public override void RenderDebug()

    .. dn:method:: Clay.Game.Mod.Entities.Vehicle.SceneryCollisionHandler(DistanceFieldCollisionInfo)



        :type info: DistanceFieldCollisionInfo


        .. code-block:: csharp

            public override void SceneryCollisionHandler(DistanceFieldCollisionInfo info)

    .. dn:method:: Clay.Game.Mod.Entities.Vehicle.SetAvoidanceMode()




        .. code-block:: csharp

            public void SetAvoidanceMode()

    .. dn:method:: Clay.Game.Mod.Entities.Vehicle.SetBehaviour(AIBehaviour)



        :type behaviour: AIBehaviour


        .. code-block:: csharp

            public void SetBehaviour(AIBehaviour behaviour)

    .. dn:method:: Clay.Game.Mod.Entities.Vehicle.SetBehaviour(System.String)



        :type behaviour: System.String


        .. code-block:: csharp

            public void SetBehaviour(string behaviour)

    .. dn:method:: Clay.Game.Mod.Entities.Vehicle.SetDefaultMaxSpeed(System.Single)



        :type value: System.Single


        .. code-block:: csharp

            public void SetDefaultMaxSpeed(float value)

    .. dn:method:: Clay.Game.Mod.Entities.Vehicle.SetDrag(System.Single)



        :type value: System.Single


        .. code-block:: csharp

            public void SetDrag(float value)

    .. dn:method:: Clay.Game.Mod.Entities.Vehicle.SetMaxAcceleration(System.Single)



        :type value: System.Single


        .. code-block:: csharp

            public void SetMaxAcceleration(float value)

    .. dn:method:: Clay.Game.Mod.Entities.Vehicle.SetMaxSpeed(System.Single)



        :type value: System.Single


        .. code-block:: csharp

            public void SetMaxSpeed(float value)

    .. dn:method:: Clay.Game.Mod.Entities.Vehicle.SetPitch(System.Single)



        :type value: System.Single


        .. code-block:: csharp

            public override void SetPitch(float value)

    .. dn:method:: Clay.Game.Mod.Entities.Vehicle.SetPitchSpeed(System.Single)



        :type value: System.Single


        .. code-block:: csharp

            public void SetPitchSpeed(float value)

    .. dn:method:: Clay.Game.Mod.Entities.Vehicle.SetSpeed(System.Single)



        :type value: System.Single


        .. code-block:: csharp

            public void SetSpeed(float value)

    .. dn:method:: Clay.Game.Mod.Entities.Vehicle.SetTargetBehaviour(AIBehaviour)



        :type behaviour: AIBehaviour


        .. code-block:: csharp

            public void SetTargetBehaviour(AIBehaviour behaviour)

    .. dn:method:: Clay.Game.Mod.Entities.Vehicle.SetTargetBehaviour(System.String)



        :type behaviour: System.String


        .. code-block:: csharp

            public void SetTargetBehaviour(string behaviour)

    .. dn:method:: Clay.Game.Mod.Entities.Vehicle.SetVisiblePitch(System.Single)



        :type value: System.Single


        .. code-block:: csharp

            public override void SetVisiblePitch(float value)

    .. dn:method:: Clay.Game.Mod.Entities.Vehicle.Trashed()




        .. code-block:: csharp

            public override void Trashed()

    .. dn:method:: Clay.Game.Mod.Entities.Vehicle.Update(System.Single)



        :type time: System.Single


        .. code-block:: csharp

            public override void Update(float time)

    .. dn:method:: Clay.Game.Mod.Entities.Vehicle.UpdateSpeed(System.Single)



        :type time: System.Single


        .. code-block:: csharp

            protected void UpdateSpeed(float time)



